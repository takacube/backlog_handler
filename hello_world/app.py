import json


def lambda_handler(event, context):
    body_str = json.loads(event["body"])
    event_type = which_event(body_str)
    if event_type == "slack":
        handle_slack_event(body_str)
    elif event_type == "backlog":
        handle_backlog_event(body_str)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }

#webhookで飛んでくるデータがslackとbacklogでどっちからなのかを判断する．
def which_event(body):
    judge_file = open("Blocks/judge_type.json", "r")
    return json.loads(judge_file)
def handle_slack_event(body_str):

    return True
def handle_backlog_event(body_str):
    return True