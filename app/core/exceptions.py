class GramAIException(Exception):
    """Base GramAI exception."""


class AIServiceException(GramAIException):
    """Raised when AI service fails."""


class SellerNotFoundException(GramAIException):
    """Seller was not found."""


class ProductNotFoundException(GramAIException):
    """Product was not found."""


class UnauthorizedException(GramAIException):
    """Authentication failed."""