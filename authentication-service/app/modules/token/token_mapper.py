from modules.token.token_dtos import TokenInfo, TokenVerify
from modules.token.token_models import TokenModel


class TokenMapper:
    def to_token_verify(self, valid: bool) -> TokenVerify:
        return TokenVerify(valid=valid)

    def to_token_info(self, token: TokenModel) -> TokenInfo:
        return TokenInfo(sub=token.sub, name=token.name, email=token.email)
