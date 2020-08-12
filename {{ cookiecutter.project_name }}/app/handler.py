import boto3

from util.templates import env

SESSION = boto3.session.Session()
TEMPLATE = env.get_template("template.html")

def handle(_event, _context):
    return {
        "statusCode": 200,
        "body": TEMPLATE.render(name="John Doe"),
        "headers": {"Content-Type": "text/html"},
    }
