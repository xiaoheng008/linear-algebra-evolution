import pathlib
import re
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]


def display_math_errors(source):
    errors = []
    in_math = False
    fence = None
    for number, line in enumerate(source.splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith(("~~~", chr(96) * 3)):
            marker = stripped[0]
            if fence is None:
                fence = marker
            elif fence == marker:
                fence = None
            continue
        if fence is not None:
            continue
        if stripped == r"\[":
            if in_math:
                errors.append((number, "nested display math"))
            in_math = True
        elif stripped == r"\]":
            if not in_math:
                errors.append((number, "display math closes without opening"))
            in_math = False
        elif in_math and re.fullmatch(r"[=-]+", stripped):
            # Goldmark parses this as a Setext heading before math rendering.
            errors.append((number, "standalone heading underline inside math"))
    if in_math:
        errors.append((len(source.splitlines()), "unclosed display math"))
    return errors


class MathMarkupTests(unittest.TestCase):
    def test_standalone_equals_is_rejected(self):
        source = "\\[\nx\n=\ny\n\\]"
        self.assertEqual(display_math_errors(source), [
            (3, "standalone heading underline inside math")
        ])

    def test_equals_with_expression_is_allowed(self):
        self.assertEqual(display_math_errors("\\[\nx\n=y\n\\]"), [])

    def test_code_examples_are_ignored(self):
        fence = chr(96) * 3
        source = f"{fence}text\n\\[\nx\n=\ny\n\\]\n{fence}"
        self.assertEqual(display_math_errors(source), [])

    def test_content_math_blocks(self):
        failures = []
        for path in sorted((ROOT / "content").rglob("*.md")):
            for number, message in display_math_errors(path.read_text()):
                failures.append(f"{path.relative_to(ROOT)}:{number}: {message}")
        self.assertFalse(failures, "\n".join(failures))


if __name__ == "__main__":
    unittest.main()
