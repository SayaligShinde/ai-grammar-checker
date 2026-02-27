from fastapi import APIRouter
import language_tool_python
from schemas import TextInput

router = APIRouter()

tool = language_tool_python.LanguageTool('en-US')

@router.post("/check-grammar")
def check_grammar(data: TextInput):
    matches = tool.check(data.text)
    corrected_text = language_tool_python.utils.correct(data.text, matches)

    errors = []

    for match in matches:
        errors.append({
            "message": match.message,
            "incorrect_text": data.text[match.offset: match.offset + match.error_length],
            "suggestions": match.replacements
        })

    return {
        "original_text": data.text,
        "corrected_text": corrected_text,
        "total_errors": len(errors),
        "errors": errors
    }
