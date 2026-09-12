import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response


class LaunchRequestHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speech = """
        <speak>
            Let's begin diaphragmatic breathing.

            Get comfortable and relax your shoulders.
            Place one hand on your chest and one hand on your stomach.

            <break time="2s"/>

            Slowly breathe in through your nose.
            <break time="4s"/>

            Now slowly breathe out through your mouth.
            <break time="6s"/>

            Again. Breathe in slowly.
            <break time="4s"/>

            And breathe out.
            <break time="6s"/>

            Breathe in.
            <break time="4s"/>

            And slowly breathe out.
            <break time="6s"/>

            One last time. Breathe in.
            <break time="4s"/>

            And breathe out.
            <break time="6s"/>

            Great job. Continue breathing naturally and allow your body to relax.
        </speak>
        """

        return (
            handler_input.response_builder
                .speak(speech)
                .set_should_end_session(True)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        return (
            handler_input.response_builder
                .speak(
                    "I can guide you through diaphragmatic breathing. "
                    "Say, Alexa, open calm breathing."
                )
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return (
            ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input)
            or ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)
        )

    def handle(self, handler_input):
        return (
            handler_input.response_builder
                .speak("Okay. Take care.")
                .set_should_end_session(True)
                .response
        )


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())

lambda_handler = sb.lambda_handler()