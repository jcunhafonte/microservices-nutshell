from fastapi_module import module


from modules.meta.meta_controller import MetaController


@module("/meta", controllers=(MetaController,))
class MetaModule:
    ...
