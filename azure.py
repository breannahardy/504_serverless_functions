import azure.functions as func
import json
import logging

# Create a FunctionApp with HTTP auth level set to 'Function'
app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="creatinine_class")
def creatinine_func(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Processing creatinine request.")

    # Try to get 'creatinine' from query parameters
    creatinine = req.params.get("creatinine")

    # If not in query params, try JSON body
    if not creatinine:
        try:
            req_body = req.get_json()
            creatinine = req_body.get("creatinine")
        except:
            pass

    # If still missing, return error
    if not creatinine:
        return func.HttpResponse(
            json.dumps({"error": "Field 'creatinine' is required."}),
            status_code=400,
            mimetype="application/json"
        )

    # Convert to float
    try:
        c_val = float(creatinine)
    except:
        return func.HttpResponse(
            json.dumps({"error": "'creatinine' must be a number."}),
            status_code=400,
            mimetype="application/json"
        )

    # Classify creatinine (adult women)
    if 0.59 <= c_val <= 1.04:
        status = "normal"
        category = "Normal (0.59–1.04 mg/dL, adult women)"
    else:
        status = "abnormal"
        category = "Abnormal (outside 0.59–1.04 mg/dL)"

    # Return JSON response
    return func.HttpResponse(
        json.dumps({
            "creatinine": c_val,
            "status": status,
            "category": category
        }),
        status_code=200,
        mimetype="application/json"
    )
