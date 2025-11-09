# compiler - AI-Enhanced Documentation

*Generated with AI-powered analysis*

## 📊 Project Statistics

| Metric | Value |
|--------|-------|
| Total Files | 23 |
| Python Files | 23 |
| Total Lines | 694 |
| Classes | 21 |
| Functions | 0 |
| Modules | 23 |

## 📑 Table of Contents

1. [__init__](#__init__)
2. [base_compiler](#base_compiler)
3. [__init__](#__init__)
4. [cpp_compiler](#cpp_compiler)
5. [csharp_compiler](#csharp_compiler)
6. [generic_compiler](#generic_compiler)
7. [go_compiler](#go_compiler)
8. [java_compiler](#java_compiler)
9. [js_compiler](#js_compiler)
10. [jython_compiler](#jython_compiler)
11. [kotlin_compiler](#kotlin_compiler)
12. [php_compiler](#php_compiler)
13. [python_compiler](#python_compiler)
14. [r_compiler](#r_compiler)
15. [ruby_compiler](#ruby_compiler)
16. [rust_compiler](#rust_compiler)
17. [swift_compiler](#swift_compiler)
18. [ts_compiler](#ts_compiler)
19. [__init__](#__init__)
20. [constant_folding](#constant_folding)
21. [peephole](#peephole)
22. [__init__](#__init__)
23. [ai_pipeline](#ai_pipeline)

## 📚 Module Documentation

## __init__.py

**Statistics:**
- 🏛️ Classes: 0
- ⚙️ Functions: 0
- 📥 Imports: 0
- 📊 Lines of Code: 0

---

## base_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 3
- 📊 Lines of Code: 0

### Classes

#### `class BaseCompiler`

**Inherits from:** `ABC`

**Location:** Line 5

**Methods (9):**
- `__init__(self, ai_model)` → `None`
- `lexical_analysis(self, code)` → `Any` [@abstractmethod]
- `syntax_analysis(self, code)` → `Any` [@abstractmethod]
- `semantic_analysis(self, ast)` → `None` [@abstractmethod]
- `intermediate_code_generation(self, ast)` → `Any` [@abstractmethod]
- ... and 4 more methods

### Dependencies

- `{'module': 'abc', 'names': ['ABC', 'abstractmethod'], 'type': 'from_import', 'lineno': 1}`
- `{'module': 'typing', 'names': ['List', 'Any'], 'type': 'from_import', 'lineno': 2}`
- `{'module': 'compiler.utils.ai_pipeline', 'names': ['AIPipeline'], 'type': 'from_import', 'lineno': 3}`

---

## compilers\__init__.py

**Statistics:**
- 🏛️ Classes: 0
- ⚙️ Functions: 0
- 📥 Imports: 0
- 📊 Lines of Code: 0

---

## compilers\cpp_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class CppCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\csharp_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class CSharpCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\generic_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 3
- 📊 Lines of Code: 0

### Classes

#### `class GenericCompiler`

**Inherits from:** `BaseCompiler`

**Location:** Line 7

**Methods (6):**
- `__init__(self, ai_model, lang_name)` → `None`
- `lexical_analysis(self, code)` → `List[...]`
- `syntax_analysis(self, code)` → `Any`
- `semantic_analysis(self, ast)` → `None`
- `intermediate_code_generation(self, ast)` → `Any`
- ... and 1 more methods

### Dependencies

- `{'module': 'typing', 'names': ['List', 'Any'], 'type': 'from_import', 'lineno': 1}`
- `{'module': 'compiler.base_compiler', 'names': ['BaseCompiler'], 'type': 'from_import', 'lineno': 3}`
- `{'module': 'compiler.optimizers.peephole', 'names': ['PeepholeOptimizer'], 'type': 'from_import', 'lineno': 4}`

---

## compilers\go_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class GoCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\java_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class JavaCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\js_compiler.py

**Statistics:**
- 🏛️ Classes: 3
- ⚙️ Functions: 0
- 📥 Imports: 5
- 📊 Lines of Code: 0

### Classes

#### `class JSParser`

**Location:** Line 9

**Methods (6):**
- `__init__(self, tokens)` → `None`
- `parse(self)` → `None`
- `parse_let(self)` → `None`
- `parse_expression(self)` → `None`
- `parse_term(self)` → `None`
- ... and 1 more methods

#### `class JSConstantFolding`

**Location:** Line 61

**Methods (3):**
- `visit(self, node)` → `None`
- `generic_visit(self, node)` → `None`
- `visit_BinaryExpression(self, node)` → `None`

#### `class JavaScriptCompiler`

**Inherits from:** `BaseCompiler`

**Location:** Line 92

**Methods (6):**
- `lexical_analysis(self, code)` → `List[...]`
- `syntax_analysis(self, code)` → `Any`
- `semantic_analysis(self, ast)` → `None`
- `intermediate_code_generation(self, ast)` → `Any`
- `code_optimization(self, ast)` → `Any`
- ... and 1 more methods

### Dependencies

- `{'module': 're', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'tokenize', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'typing', 'names': ['Any', 'List'], 'type': 'from_import', 'lineno': 4}`
- `{'module': 'compiler.base_compiler', 'names': ['BaseCompiler'], 'type': 'from_import', 'lineno': 6}`

---

## compilers\jython_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 2
- 📊 Lines of Code: 0

### Classes

#### `class JythonCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 6

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 3}`

---

## compilers\kotlin_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class KotlinCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\php_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 2
- 📊 Lines of Code: 0

### Classes

#### `class PhpCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 6

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 3}`

---

## compilers\python_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 7
- 📊 Lines of Code: 0

### Classes

#### `class PythonCompiler`

**Inherits from:** `BaseCompiler`

**Location:** Line 11

**Methods (6):**
- `lexical_analysis(self, code)` → `List[...]`
- `syntax_analysis(self, code)` → `ast.AST`
- `semantic_analysis(self, ast_tree)` → `None`
- `code_optimization(self, ast_tree)` → `ast.AST`
- `intermediate_code_generation(self, ast)` → `Any`
- ... and 1 more methods

### Dependencies

- `{'module': 'ast', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'io', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'tokenize', 'alias': None, 'type': 'import', 'lineno': 4}`
- `{'module': 'typing', 'names': ['Any', 'List'], 'type': 'from_import', 'lineno': 5}`
- `{'module': 'compiler.base_compiler', 'names': ['BaseCompiler'], 'type': 'from_import', 'lineno': 7}`
- `{'module': 'compiler.optimizers.constant_folding', 'names': ['ConstantFolding'], 'type': 'from_import', 'lineno': 8}`

---

## compilers\r_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 2
- 📊 Lines of Code: 0

### Classes

#### `class RCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 6

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 3}`

---

## compilers\ruby_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 2
- 📊 Lines of Code: 0

### Classes

#### `class RubyCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 6

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 3}`

---

## compilers\rust_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class RustCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\swift_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 4
- 📊 Lines of Code: 0

### Classes

#### `class SwiftCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 8

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'tempfile', 'alias': None, 'type': 'import', 'lineno': 2}`
- `{'module': 'os', 'alias': None, 'type': 'import', 'lineno': 3}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 5}`

---

## compilers\ts_compiler.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 2
- 📊 Lines of Code: 0

### Classes

#### `class TypeScriptCompiler`

**Inherits from:** `GenericCompiler`

**Location:** Line 6

**Methods (2):**
- `__init__(self, ai_model)` → `None`
- `execute(self, code)` → `None`

### Dependencies

- `{'module': 'subprocess', 'alias': None, 'type': 'import', 'lineno': 1}`
- `{'module': 'compiler.compilers.generic_compiler', 'names': ['GenericCompiler'], 'type': 'from_import', 'lineno': 3}`

---

## optimizers\__init__.py

**Statistics:**
- 🏛️ Classes: 0
- ⚙️ Functions: 0
- 📥 Imports: 0
- 📊 Lines of Code: 0

---

## optimizers\constant_folding.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 1
- 📊 Lines of Code: 0

### Classes

#### `class ConstantFolding`

**Inherits from:** `ast.NodeTransformer`

**Location:** Line 3

**Methods (1):**
- `visit_BinOp(self, node)` → `None`

### Dependencies

- `{'module': 'ast', 'alias': None, 'type': 'import', 'lineno': 1}`

---

## optimizers\peephole.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 0
- 📊 Lines of Code: 0

### Classes

#### `class PeepholeOptimizer`

**Location:** Line 1

**Methods (2):**
- `__init__(self, tokens)` → `None`
- `optimize(self)` → `None`

---

## utils\__init__.py

**Statistics:**
- 🏛️ Classes: 0
- ⚙️ Functions: 0
- 📥 Imports: 0
- 📊 Lines of Code: 0

---

## utils\ai_pipeline.py

**Statistics:**
- 🏛️ Classes: 1
- ⚙️ Functions: 0
- 📥 Imports: 1
- 📊 Lines of Code: 0

### Classes

#### `class AIPipeline`

**Location:** Line 4

**Methods (2):**
- `__init__(self, model_name)` → `None`
- `__call__(self, prompt)` → `List[...]`

### Dependencies

- `{'module': 'typing', 'names': ['List', 'Dict'], 'type': 'from_import', 'lineno': 1}`

---

## 🏗️ Architecture Overview

### Module Dependencies

**Internal Dependencies:**

- `compilers\cpp_compiler.py` → compiler
- `compilers\csharp_compiler.py` → compiler
- `compilers\generic_compiler.py` → compiler
- `compilers\go_compiler.py` → compiler
- `compilers\java_compiler.py` → compiler

**External Dependencies:**

- `abc`
- `ast`
- `io`
- `os`
- `re`
- `subprocess`
- `tempfile`
- `tokenize`
- `typing`
