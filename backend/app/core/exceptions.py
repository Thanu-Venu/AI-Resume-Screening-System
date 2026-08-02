class AppException(Exception):
    """Base class for all application level exception (doesnt include finenotfound,zerodivisionerror)"""
    pass

class NotFoundException(AppException):
    """Base class for all resource not found exceptions."""
    pass

class JobNotFoundException(NotFoundException):
    """Raised when a requested job cannot be found."""

    def __init__(self, job_id: int):
        self.job_id = job_id
        super().__init__(f"Job with ID {job_id} was not found.")

