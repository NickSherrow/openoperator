from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass
from typing import Any, Dict, Optional

@dataclass
class BaseTelemetryEvent(ABC):
	@property
	@abstractmethod
	def name(self) -> str:
		pass

	@property
	def properties(self) -> Dict[str, Any]:
		return {k: v for k, v in asdict(self).items() if k != 'name'}


@dataclass
class RegisteredFunction:
	name: str
	params: dict[str, Any]


@dataclass
class ControllerRegisteredFunctionsTelemetryEvent(BaseTelemetryEvent):
	registered_functions: list[RegisteredFunction]
	name: str = 'controller_registered_functions'


@dataclass
class BrowserActionEvent(BaseTelemetryEvent):
	action_name: str
	action_params: Dict[str, Any]
	success: bool
	error: Optional[str] = None
	name: str = 'browser_action'


@dataclass
class BrowserNavigationEvent(BaseTelemetryEvent):
	url: str
	success: bool
	error: Optional[str] = None
	name: str = 'browser_navigation'
