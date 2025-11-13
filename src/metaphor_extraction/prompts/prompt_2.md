You are an expert linguist analyzing medical conversation transcripts for metaphors. The document follows this structure:

- Main sections: **H0**, **H1**, **H2**, etc.
- Subsections: H0-1, H0-2, H1-1, H1-2, etc.
- Speaker codes: P: (Patient), N: (Family/Naaste), O: (Researcher/Onderzoeker)

## CRITICAL EXTRACTION PROTOCOL

### Step 1: Document Structure Verification

Before any analysis:

1. Scan the ENTIRE document to identify all section markers
2. List all sections found (e.g., H0, H0-1, H0-2, H1, H1-1)
3. Note the speaker pattern (P:, N:, O:)

### Step 2: Understanding Metaphors with Examples

A metaphor occurs when one concept (target domain) is described using another (source domain). Study these verified examples from cancer discourse research:

**FAIRGROUND RIDES metaphors:**

- "Imagine it a bit like a scary fairground ride – it might be scary in places, but it will eventually stop and you can get off. Be strong, be brave and we will be here to hold your hand if you need it."

**JOURNEY metaphors:**

- "My journey with cancer may not be smooth but it certainly makes me look up and take notice of the scenery!"
- "Some journeys with cancer will be longer and others short, but what matters most is how we walk that journey."
- "Cancer is a hard journey with many twists and turns. No two people go through the exact same route. It’s like driving a horse-drawn coach without the back wheels. It’s helpful to occasionally stop, rest the horses, and review the situation with someone you are close to."
- "The rocks in our path are easier to handle when we are all in it together. The best people to help you are the ones who have been there before you or are heading there with you."

**STONE IN YOUR SHOE metaphors:**

- "I compare life after cancer to walking with a stone in your shoe. If you let the stone rest right under the sole of your foot, it hurts every time you take a step and it is hard to move forward. But if you can manoeuvre the stone to sit between your toes, it is still there but you can walk the fine line of life without hurting."

**FIGHTING metaphors:**

- "I don’t intend to give up; I don’t intend to give in. No I want to fight it. I don’t want it to beat me, I want to beat it."
- "I respect Cancer and never underestimate the power it has, but, if you can face up to it and hit it back head on, you stand a good chance of beating it for a bit longer."

**NOT-FIGHTING/RELATIONSHIP metaphors:**

- "Having cancer is not a fight but a relationship where I am forced to live with my disease day in, day out. Some days cancer has the upper hand, other days I do."
- "‘Battle’ suggests either I win or cancer does. I think of it more as ‘working with cancer’. For me, seen in this more everyday way, the cancer becomes easier to cope with."
- "You fight this terrible, faceless illness that has invaded every part of you. You stand and say, ‘No, this is not all there is to me’. You have fought back, taken control of the things left to you. And even when you felt crap, you forced yourself to get out of bed and keep going."

**MUSIC metaphors:**

- "Cancer is part of me, the cure for cancer is accepting it, to heal is to convince the cancer cells to sing in tune with the rest of the body."

**INVASION metaphors:**

- "For me, cancer arrived as an unwelcome lodger, parking itself in the back room and demanding attention. I tried to be a courteous if unwilling host until eventually the time came to invite my cancer to leave. It has left the place in a bit of a mess, and I’m conscious that it has kept the key. Still I’m hopeful that in due course all I will be left with is the rich memory of time spent with a stranger I never expected to meet."
- "Initially, cancer feels like an alien invasion. It is as if you want to strip off your body and get a new one. Then in time, you ‘connect’ with it somehow."

**NEW VALUE metaphors:**

- "Cancer makes me appreciate everything just a little bit more. Previously normal, everyday experiences suddenly take on a new value."

**NATURE metaphors:**

- "Cancerous tissue is like a garden that has become overgrown with weeds. The weed-killer also damages the healthy plants, but you hope they will re-grow."
- "My way of dealing with my diagnosis is to ‘bend with the wind’"

### Step 3: Extraction Requirements

For EVERY potential metaphor:

**VERIFICATION CHECKLIST:**
□ Can I find this EXACT text in the document?
□ Can I identify the exact section (H0-1, etc.)?
□ Can I identify the speaker (P:, N:, or O:)?
□ Is this actually metaphorical (not literal medical terminology)?

If ANY box is unchecked → SKIP THIS ITEM

**EXTRACTION TEMPLATE:**

```
LOCATION VERIFICATION:
Section ID: [exact section like "H0-1"]
Speaker: [P: or N: or O:]
Line begins with: [first 10 words of the speaker's turn]

EXACT TEXT EXTRACTION:
Context before (20-30 words): [exact text preceding the metaphor]
METAPHOR QUOTE: [EXACT text, including typos/errors]
Context after (20-30 words): [exact text following the metaphor]

FULL VERIFICATION:
Complete sentence/turn: [the entire speaker turn containing this metaphor]
```

### Step 4: Analysis Classification

After extracting the exact text, classify according to:

**METAPHOR TYPE:**

- word: Single metaphorical word ("battle")
- phrase: 2-5 word expression ("rocky road")
- sentence: Complete metaphorical sentence
- extended: Multiple sentences developing same metaphor

**SOURCE DOMAIN** (based on examples above):

- violence_fighting: battle, war, fight, weapon, enemy, invasion
- journey_travel: path, road, journey, destination, steps, rocks in path
- nature_garden: weeds, growth, seasons, wind, storms
- games_sports: race, match, winning, losing
- music: harmony, tune, rhythm, discord
- fairground_rides: rollercoaster, scary ride, ups and downs
- unwanted_guests: lodger, visitor, uninvited guest
- religion_supernatural: hell, demons, miracle, blessing
- restraint_control: chains, freedom, trapped, escape
- building_construction: foundation, structure, rebuild
- machine_technology: broken, repair, malfunction, system
- other: (only if none of the above fit)

**FUNCTION IN CONTEXT:**

- explanation: Making medical concepts understandable
- coping: Managing emotional response
- empowerment: Building sense of control/agency
- relationship: Describing connection with disease
- prognosis: Discussing future/outcomes
- treatment: Describing medical interventions
- emotion_expression: Conveying feelings
- humor: Using humor to cope

### Step 5: Quality Control

**NEVER Include:**

- Paraphrased or reconstructed quotes
- Combined fragments from different places
- Cleaned-up versions of messy speech
- Metaphors you "think" are there but can't locate exactly

**AVOID Common Errors:**

- "Tumor growth" = literal medical term, NOT metaphor
- "Cancer spreading" = medical terminology, NOT metaphor
- "Spreading like wildfire" = IS a metaphor
- "Treatment process" = literal, NOT metaphor
- "Treatment journey" = IS a metaphor

**Priority Order:**

1. Clear, explicit metaphors matching the examples
2. Extended metaphors developed over multiple sentences
3. Novel/creative metaphors unique to this speaker
4. Conventional metaphors (only if clearly identifiable)

### Step 6: Structured Output Requirements

For each VERIFIED metaphor, provide:

**location:**

- section_id: Exact section (e.g., "H0-1")
- speaker_turn: Speaker code ("P:", "N:", or "O:")
- context_before: 20-30 words before (EXACT text)
- context_after: 20-30 words after (EXACT text)

**metaphor fields:**

- original_quote: EXACT metaphor text from document
- translation_quote: English translation if Dutch
- quote_verification: Complete sentence containing the metaphor
- metaphor_type: word/phrase/sentence/extended
- source_domain: From list above
- metaphor_function: From list above
- description: What this metaphor means in context
- reasoning: Why this is metaphorical (not literal)
- confidence_score: 1-10 (10=definitely metaphor, 1=possibly)

## DOCUMENT TO ANALYZE

{document_text}

## FINAL EXECUTION INSTRUCTIONS

1. First output: List all sections you found in the document
2. Process each section systematically
3. For each speaker turn, check for metaphorical language
4. Apply verification checklist before including anything
5. Extract only verifiable quotes with exact location
6. Classify based on the examples provided
7. Output complete structured data for each verified metaphor

Remember: 3 accurately extracted metaphors are more valuable than 20 with any fabrication or uncertainty. Quality over quantity.
