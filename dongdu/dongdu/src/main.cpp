/**
 * @file main.cpp
 * @author Hoàng Văn Khoa <hoangvankhoa@outlook.com>
 */

#include <Python.h>
#include <string>
#include <iostream>
#include "Machine.h"
#include "main.h"

static dongdu::Machine predictor;

static PyObject * hello(PyObject *self, PyObject *args)
{
    std::cout << "Hello World!\n";
    return args;
}

static PyObject * segment(PyObject *self, PyObject *args)
{
	const char *inputStr;
	if (!PyArg_ParseTuple(args, "s", &inputStr))
        return NULL;
	return PyUnicode_FromString(predictor.segment(inputStr).c_str());
}

PyMODINIT_FUNC PyInit_dongdu_native(void)
{
    std::cout << "Initializing . . . \n";

	PyObject * pyDongDuModule = PyImport_ImportModule("dongdu");
	PyObject * pyDataPath = PyObject_GetAttrString(pyDongDuModule, "__data_path__");
	if (pyDataPath == NULL)
	{
		std::cerr << "Initializing was unsuccessful! Failed to find data path!\n";
		return NULL;
	}

    char * dataDir = PyUnicode_AsUTF8(pyDataPath);
    if (dataDir == NULL)
    {
    	std::cerr << "Initializing was unsuccessful! Cannot get data path!\n";
		return NULL;
    }
	std::string strInput = "Đây là một ví dụ đơn giản minh họa cho việc sử dụng công cụ Đông Du để tách từ.";
	std::cout << "Begin initializing data for dongdu . . .\n";
	predictor.init(3, dataDir, dongdu::PREDICT);
	if (!predictor.load())
	{
		std::cerr << "Initializing was unsuccessful!\n";
		return NULL;
	}
	std::cout << "Initializing has been completed!\n";
	std::cout << "Input example: " << strInput << "\n";
	std::string strOutput = predictor.segment(strInput);
	std::cout << "Output example: " << strOutput << "\n";
    return PyModule_Create(&dongDuModule);
}

int main(int argc, char *argv[])
{
    /* Add a built-in module, before Py_Initialize */
    PyImport_AppendInittab("dongdu_native", PyInit_dongdu_native);

    /* Initialize the Python interpreter.  Required. */
    Py_Initialize();

    /* Optionally import the module; alternatively,
       import can be deferred until the embedded script
       imports it. */
    PyImport_ImportModule("dongdu_native");
    return 0;
}
