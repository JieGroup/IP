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
    List[Any]
]

Database_Type = Literal[
    'survey_answer',
    'survey_summary',
    'survey_template',
    'voter'
]

Survey_Update_Method = Literal[
    'static'
    'uniform',
]

MTurkID = Literal['str']

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