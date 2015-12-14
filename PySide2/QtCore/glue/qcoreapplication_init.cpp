// Global variables used to store argc and argv values
static int QCoreApplicationArgCount;
static char** QCoreApplicationArgValues;

bool QCoreApplicationConstructorStart(PyObject* argv)
{
    if (QCoreApplication::instance()) {
        PyErr_SetString(PyExc_RuntimeError, "A QCoreApplication instance already exists.");
        return false;
    }

    return Shiboken::sequenceToArgcArgv(argv, &QCoreApplicationArgCount, &QCoreApplicationArgValues, "PySideApp");
}

void QCoreApplicationConstructorEnd(PyObject* self)
{
    PySide::registerCleanupFunction(&PySide::destroyQCoreApplication);
    Py_INCREF(self);
}

void QCoreApplicationConstructor(PyObject* self, PyObject* argv, QCoreApplicationWrapper** cptr)
{
    if (QCoreApplicationConstructorStart(argv)) {
        *cptr = new QCoreApplicationWrapper(QCoreApplicationArgCount, QCoreApplicationArgValues);
        Shiboken::Object::releaseOwnership(reinterpret_cast<SbkObject*>(self));
        QCoreApplicationConstructorEnd(self);
    }
}
