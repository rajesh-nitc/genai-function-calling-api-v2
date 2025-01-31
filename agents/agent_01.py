from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.function_choice_behavior import (
    FunctionChoiceBehavior,
)
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.kernel import Kernel

from config.settings import settings
from plugins.add_plugins import add_plugins


async def get_agent_01():
    kernel = Kernel()
    add_plugins(kernel)

    service_id = "agent"
    agent_name = "agent_01"

    kernel.add_service(
        AzureChatCompletion(
            service_id=service_id,
            api_key=settings.AZURE_OPENAI_API_KEY,
            endpoint=settings.AZURE_OPENAI_ENDPOINT,
            deployment_name=settings.LLM_MODEL,
        )
    )

    execution_settings = kernel.get_prompt_execution_settings_from_service_id(
        service_id=service_id
    )
    execution_settings.function_choice_behavior = FunctionChoiceBehavior.Auto()
    return ChatCompletionAgent(
        service_id=service_id,
        kernel=kernel,
        name=agent_name,
        instructions=settings.LLM_SYSTEM_INSTRUCTION,
        execution_settings=execution_settings,
    )
