/**
 * @file main.cpp
 * @author Hoàng Văn Khoa <hoangvankhoa@outlook.com>
 */

static PyObject * hello(PyObject * self, PyObject * args);
static PyObject * segment(PyObject * self, PyObject * args);

static PyMethodDef dongDuMethods[] = {
    {"hello",  hello, METH_VARARGS, "Say hello."},
    {"segment", segment, METH_VARARGS, "Phân tách từ Tiếng Việt"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef dongDuModule = {
    PyModuleDef_HEAD_INIT,
    "dongdu_native",       /* name of module */
    "Hỗ trợ tách từ dành cho tiếng Việt", /* module documentation, may be NULL */
    -1,             /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    dongDuMethods,  /* m_methods */
    NULL,           /* m_reload */
    NULL,           /* m_traverse */
    NULL,           /* m_clear */
    NULL,           /* m_free */
};