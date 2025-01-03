"""
Code for Agents.
"""
from .agent import Agent, AgentOptions, AgentCallbacks, AgentProcessingResult, AgentResponse
from .lambda_agent import LambdaAgent, LambdaAgentOptions
from .bedrock_llm_agent import BedrockLLMAgent, BedrockLLMAgentOptions
from .lex_bot_agent import LexBotAgent, LexBotAgentOptions
from .amazon_bedrock_agent import AmazonBedrockAgent, AmazonBedrockAgentOptions
from .comprehend_filter_agent import ComprehendFilterAgent, ComprehendFilterAgentOptions
from .chain_agent import ChainAgent, ChainAgentOptions
from .bedrock_translator_agent import BedrockTranslatorAgent, BedrockTranslatorAgentOptions
from .bedrock_inline_agent import BedrockInlineAgent, BedrockInlineAgentOptions

try:
    from .anthropic_agent import AnthropicAgent, AnthropicAgentOptions
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False


__all__ = [
    'Agent',
    'AgentOptions',
    'AgentCallbacks',
    'AgentProcessingResult',
    'AgentResponse',
    'LambdaAgent',
    'LambdaAgentOptions',
    'BedrockLLMAgent',
    'BedrockLLMAgentOptions',
    'LexBotAgent',
    'LexBotAgentOptions',
    'AmazonBedrockAgent',
    'AmazonBedrockAgentOptions',
    'ComprehendFilterAgent',
    'ComprehendFilterAgentOptions',
    'BedrockTranslatorAgent',
    'BedrockTranslatorAgentOptions',
    'ChainAgent',
    'ChainAgentOptions',
    'BedrockInlineAgent',
    'BedrockInlineAgentOptions'
]

if _ANTHROPIC_AVAILABLE:
    __all__.extend([
        'AnthropicAgent',
        'AnthropicAgentOptions'
    ])
