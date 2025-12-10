import json
import functions_framework

@functions_framework.http
def creatinine_class(request):
    """
    HTTP Cloud Function.
    Expects JSON with 'creatinine' (or query param as fallback).
    Returns a JSON classification of creatinine level.
    """

    # Prefer JSON body; fall back to query parameters
    data = request.get_json(silent=True) or {}
    args = request.args or {}

    creatinine = data.get("creatinine", args.get("creatinine"))

    # Presence check
    if creatinine is None:
        return (
            json.dumps({"error": "'creatinine' is required."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Type / convert check
    try:
        c_val = float(creatinine)
    except (TypeError, ValueError):
        return (
            json.dumps({"error": "'creatinine' must be numeric."}),
            400,
            {"Content-Type": "application/json"},
        )

    # Classification rule
    status = "normal" if 0.59 <= c_val <= 1.04 else "abnormal"
    category = "Normal (0.59-1.04 mg/dL, adult women)" if status == "normal" else "Abnormal"

    payload = {
        "creatinine": c_val,
        "status": status,
        "category": category,
    }

    return json.dumps(payload), 200, {"Content-Type": "application/json"}
