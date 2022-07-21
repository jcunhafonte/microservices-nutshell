from fastapi_module import module


from modules.reports.reports_controller import ReportsController


@module("/reports", controllers=(ReportsController,))
class ReportsModule:
    ...
