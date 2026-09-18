#include "ui/appwindow.h"

#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    AppWindow w;
    w.show();
    return QApplication::exec();
}
