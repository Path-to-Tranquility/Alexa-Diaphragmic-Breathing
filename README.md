# Alexa Diaphragmatic Breathing Skill

This project creates a simple Alexa skill that guides users through a diaphragmatic breathing exercise.

Alexa gives breathing instructions and pauses between each inhale and exhale.

## How to Set It Up

1. Go to the **Alexa Developer Console**.

2. Click **Create Skill**.

3. Give your skill a name such as:

```text
Diaphragmatic Breathing
```

4. Select:

```text
Custom
```

as the skill type.

5. Choose:

```text
Alexa-Hosted (Python)
```

as the hosting option.

6. Open the skill and go to:

```text
Build → Interaction Model → Invocation
```

7. Set the invocation name to:

```text
calm breathing
```

8. Click **Save Model** and then **Build Model**.

9. Go to the **Code** tab.

10. Open:

```text
lambda_function.py
```

11. Add the Python code lanbda_function.py that is in this repo. It handles the Alexa `LaunchRequest` and provides the breathing instructions.


12. Click **Deploy** after adding the Python code.

13. Go to the **Test** tab.

14. Change the testing option from:

```text
Off
```

to:

```text
Development
```

15. Test the skill by saying:

```text
Alexa, open calm breathing
```

16. Make sure your Echo device and Alexa Developer Console use the same Amazon account.

17. Open the Alexa app and enable the development skill if required.

18. Now say:

```text
Alexa, open calm breathing
```

Alexa will guide you through the diaphragmatic breathing exercise.


## Customization

You can easily modify:

* Number of breathing rounds
* Inhale duration
* Exhale duration
* Relaxation instructions
* Opening and closing messages
* Alexa invocation name

For example, you can change:

```xml
<break time="4s"/>
```

to:

```xml
<break time="5s"/>
```

to increase the breathing duration.

## Goal

The goal of this project is to provide a simple hands-free breathing exercise that can be started anytime using Alexa.

```text
Alexa, open calm breathing
```
