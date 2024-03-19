from infra.services.api_gateway import APIGateway
from infra.services.aws_lambda import AWSLambda
from lambda_forge import service


@service
class Services:
    def __init__(self, scope, stage, arns) -> None:
        self.api_gateway = APIGateway(scope, stage)
        self.aws_lambda = AWSLambda(scope, stage)
