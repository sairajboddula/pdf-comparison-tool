# API Reference

Complete API documentation for all modules and classes.

## `__init__.py`

---

## `base_compiler.py`

### class `BaseCompiler`

**`__init__(self, ai_model)`**

**`lexical_analysis(self, code)`**

**`syntax_analysis(self, code)`**

**`semantic_analysis(self, ast)`**

**`intermediate_code_generation(self, ast)`**

**`code_optimization(self, tokens)`**

**`execute(self, code)`**

**`compile_and_run(self, code)`**

**`_recover_error(self, code, error_message)`**

---

## `compilers\__init__.py`

---

## `compilers\cpp_compiler.py`

### class `CppCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\csharp_compiler.py`

### class `CSharpCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\generic_compiler.py`

### class `GenericCompiler`

**`__init__(self, ai_model, lang_name)`**

**`lexical_analysis(self, code)`**

**`syntax_analysis(self, code)`**

**`semantic_analysis(self, ast)`**

**`intermediate_code_generation(self, ast)`**

**`code_optimization(self, tokens)`**

---

## `compilers\go_compiler.py`

### class `GoCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\java_compiler.py`

### class `JavaCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\js_compiler.py`

### class `JSParser`

**`__init__(self, tokens)`**

**`parse(self)`**

**`parse_let(self)`**

**`parse_expression(self)`**

**`parse_term(self)`**

**`parse_factor(self)`**

### class `JSConstantFolding`

**`visit(self, node)`**

**`generic_visit(self, node)`**

**`visit_BinaryExpression(self, node)`**

### class `JavaScriptCompiler`

**`lexical_analysis(self, code)`**

**`syntax_analysis(self, code)`**

**`semantic_analysis(self, ast)`**

**`intermediate_code_generation(self, ast)`**

**`code_optimization(self, ast)`**

**`execute(self, code)`**

---

## `compilers\jython_compiler.py`

### class `JythonCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\kotlin_compiler.py`

### class `KotlinCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\php_compiler.py`

### class `PhpCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\python_compiler.py`

### class `PythonCompiler`

**`lexical_analysis(self, code)`**

**`syntax_analysis(self, code)`**

**`semantic_analysis(self, ast_tree)`**

**`code_optimization(self, ast_tree)`**

**`intermediate_code_generation(self, ast)`**

**`execute(self, code)`**

---

## `compilers\r_compiler.py`

### class `RCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\ruby_compiler.py`

### class `RubyCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\rust_compiler.py`

### class `RustCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\swift_compiler.py`

### class `SwiftCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `compilers\ts_compiler.py`

### class `TypeScriptCompiler`

**`__init__(self, ai_model)`**

**`execute(self, code)`**

---

## `optimizers\__init__.py`

---

## `optimizers\constant_folding.py`

### class `ConstantFolding`

**`visit_BinOp(self, node)`**

---

## `optimizers\peephole.py`

### class `PeepholeOptimizer`

**`__init__(self, tokens)`**

**`optimize(self)`**

---

## `utils\__init__.py`

---

## `utils\ai_pipeline.py`

### class `AIPipeline`

**`__init__(self, model_name)`**

**`__call__(self, prompt)`**

---

