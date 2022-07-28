from fastapi import Depends
from fastapi_module import InferringRouter, controller


from modules.token.token_dtos import TokenInfo, TokenVerify
from modules.token.token_mapper import TokenMapper
from modules.token.token_service import TokenService
from modules.token.token_deps import get_current_token


router = InferringRouter(tags=["Token"])


@controller(router, version=1.1)
class TokenController:
    token_service: TokenService = Depends()
    token_mapper: TokenMapper = Depends()

    @router.get("/verify")
    async def get_verify(self, token: TokenInfo = Depends(get_current_token)) -> TokenVerify:
        """
        **Get verify**

        `:return: verify`
        """
        return self.token_mapper.to_token_verify(True)

    @router.get("/info")
    async def get_info(self, token: TokenInfo = Depends(get_current_token)) -> TokenInfo:
        """
        **Get info**

        `:return: info`
        """
        return self.token_mapper.to_token_info(token)
