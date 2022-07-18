from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Hashable,
    Iterator,
    Literal,
    Mapping,
    Optional,
    Protocol,
    Sequence,
    TypeVar,
    Union,
    List,
    Dict
)

JSONType = Union[
    Dict[str, Any],
    List[Any],
    str
]

Database_Type = Literal[
    'survey_answer',
    'survey_summary',
    'survey_template',
    'voter',
    'user'
]

Survey_Update_Method = Literal[
    'static',
    'uniform',
]

Answer_Type = Literal[
    'categorical',
    'continuous'
]

# must be one of the three types
# Categorical_Option_Type = TypeVar('Categorical_Option_Type', int, float, str)
Categorical_Option_Type = Union[
    int, 
    float, 
    str
]

# must be one of the two types
# Continuous_Option_Type = TypeVar('Continuous_Option_Type', int, float)
Continuous_Option_Type = Union[int, float, str]

# The Criteria of the survey topics that stores in survey template db
Survey_Topics = dict[str, dict[str, Any]]

# The answer uploaded by the voter from the last round
# If current round is 1, the Survey_Prev_Answers is an empty dict
Survey_Prev_Answers = Union[dict, dict[str, dict[str, Any]]]

# The answer uploaded by the voter from the current round
Survey_New_Answers = dict[str, Union[str, dict[str, Any]]]

Role = Literal[
    'user',
    'voter'
]

MTurkID = str

Serializable_Datatype = Union[
    dict,
    list,
    tuple,
    str,
    int,
    float,
    bool,
    None,
]
