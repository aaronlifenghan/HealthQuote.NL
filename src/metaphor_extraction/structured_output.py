"""
Structured output definitions for metaphor extraction in doctor-patient conversations
Based on Lancaster University cancer metaphor research methodology
"""

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MetaphorLocation(BaseModel):
    """Track exact location of metaphor in document"""

    section_id: str = Field(
        ..., description="Section identifier (e.g., 'H0-1', 'H1-3')"
    )
    speaker_turn: Optional[str] = Field(
        None, description="Speaker identifier for this turn (P:, N:, O:)"
    )
    context_before: str = Field(
        ..., description="20-30 words before the metaphor for verification"
    )
    context_after: str = Field(
        ..., description="20-30 words after the metaphor for verification"
    )


class MetaphorType(str, Enum):
    """Types of metaphor based on linguistic form"""

    WORD = "word"  # Single metaphorical word
    PHRASE = "phrase"  # Short metaphorical expression
    SENTENCE = "sentence"  # Full sentence with metaphorical content
    EXTENDED = "extended"  # Multi-sentence metaphorical narrative


class SourceDomain(str, Enum):
    """Source domains based on Lancaster University cancer metaphor research"""

    VIOLENCE_FIGHTING = "violence_fighting"  # battle, fight, weapon, enemy
    JOURNEY_TRAVEL = "journey_travel"  # journey, road, path, destination
    NATURE_GARDEN = "nature_garden"  # weeds, growth, seasons
    GAMES_SPORTS = "games_sports"  # marathon, sprint, winning, losing
    MUSIC = "music"  # harmony, tune, rhythm
    FAIRGROUND_RIDES = "fairground_rides"  # rollercoaster, scary ride
    UNWANTED_GUESTS = "unwanted_guests"  # lodger, visitor, invasion
    RELIGION_SUPERNATURAL = "religion_supernatural"  # hell, limbo, demons
    RESTRAINT_CONTROL = "restraint_control"  # chains, freedom, escape
    BUILDING_CONSTRUCTION = "building_construction"  # foundation, structure
    MACHINE_TECHNOLOGY = "machine_technology"  # breakdown, repair, malfunction
    OTHER = "other"  # For metaphors not fitting above categories


class MetaphorFunction(str, Enum):
    """What the metaphor is being used to accomplish"""

    EXPLANATION = "explanation"  # Doctor explaining medical concepts
    COPING = "coping"  # Patient dealing with emotions/situation
    EMPOWERMENT = "empowerment"  # Building sense of agency/control
    RELATIONSHIP = "relationship"  # Describing patient-disease relationship
    PROGNOSIS = "prognosis"  # Discussing future outcomes
    TREATMENT = "treatment"  # Describing medical interventions
    EMOTION_EXPRESSION = "emotion_expression"  # Expressing feelings
    HUMOR = "humor"  # Using humor to cope
    OTHER = "other"


class Metaphor(BaseModel):
    """
    Comprehensive metaphor analysis class for doctor-patient conversations
    Based on Lancaster University cancer metaphor research methodology
    """

    # Location information - MUST BE FIRST
    location: MetaphorLocation = Field(
        ..., description="Exact location information for verification"
    )

    # Core identification
    original_quote: str = Field(
        ...,
        description="EXACT text as it appears in the document - no modifications",
    )

    translation_quote: str = Field(
        ..., description="English translation if original is in Dutch"
    )

    # Verification field
    quote_verification: str = Field(
        ...,
        description="Full sentence/paragraph containing the quote for context",
    )

    # Metaphor classification
    metaphor_type: MetaphorType = Field(
        ..., description="Linguistic form of the metaphor"
    )
    source_domain: SourceDomain = Field(
        ..., description="Conceptual source domain of the metaphor"
    )

    metaphor_function: MetaphorFunction = Field(
        ..., description="Purpose/function of the metaphor in context"
    )

    # Analysis fields
    description: str = Field(
        ..., description="Clear explanation of the metaphor and its meaning"
    )
    reasoning: str = Field(
        ..., description="Justification for identifying this as a metaphor"
    )
    confidence_score: int = Field(
        ...,
        ge=1,
        le=10,
        description="Confidence in metaphor identification (1-10)",
    )

    class Config:
        use_enum_values = True


class MetaphorsResponse(BaseModel):
    metaphors: List[Metaphor] = Field(
        ..., description="List of identified metaphors with detailed analysis"
    )
