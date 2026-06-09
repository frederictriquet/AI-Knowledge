> Source : https://embracethered.com/blog/posts/2024/ascii-smuggling-and-hidden-prompt-instructions/
> Auteur : Johann Rehberger (Embrace The Red)

# Embrace The Red

# Video: ASCII Smuggling and Hidden Prompt Instructions

Posted on Feb 12, 2024

[\#aiml](https://embracethered.com/blog//tags/aiml) [\#machine learning](https://embracethered.com/blog//tags/machine-learning) [\#threats](https://embracethered.com/blog//tags/threats) [\#bugbounty](https://embracethered.com/blog//tags/bugbounty) [\#llm](https://embracethered.com/blog//tags/llm) [\#video](https://embracethered.com/blog//tags/video)

A couple of weeks ago hidden prompt injections were discovered and [we covered it at the time](https://embracethered.com/blog/posts/2024/hiding-and-finding-text-with-unicode-tags/).

This video explains it in more detail, and also highlights implications beyond hiding instructions, including what I call `ASCII Smuggling`. This is the usage of [Unicode Tags Block characters](https://en.wikipedia.org/wiki/Tags_(Unicode_block)) to both craft and deciper hidden messages in plain sight.

# Une erreur s'est produite.

Impossible d'exécuter JavaScript.

\
\

Using Unicode encoding to bypass security features or execute code (XSS, SSRF,..) has been in use for a while, however this new TTP enables more sophisticated attack scenarios.

This is because Unicode Tags Code Point mirror the entire ASCII set, but are often not visible in UI elements. For Large Language Models this is interesting because LLMs often interpret this hidden text as ASCII, and they can also craft such hidden text when replying to user queries.

### Take-aways

Couple of things come to mind and I touch on those in the video in more detail:

- Test your own LLM apps for this new attack vector
- As developer a possible mitigations is to remove Unicode Tags Block text on the way in and out
- Consider implications beyond LLM applications and Chatbots\
  \

### The ASCII Smuggler Tool is here by the way

[![ASCII Smuggler Tool](https://embracethered.com/blog/images/2024/ascii-smuggler-qr-clean.png)](https://embracethered.com/blog/ascii-smuggler.html)

------------------------------------------------------------------------

- [Newer →](https://embracethered.com/blog/posts/2024/lack-of-isolation-gpts-code-interpreter/)
- [  Contact me](mailto:security@wunderwuzzi.net)
- [← Older](https://embracethered.com/blog/posts/2024/claude-hidden-prompt-injection-ascii-smuggling/)
