#include "ui/appwindow.h"
#include "./ui_appwindow.h"
#include <QWebEngineView>

AppWindow::AppWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::AppWindow)
{
    setWindowTitle("ReadItLoud");
    ui->setupUi(this);
}

AppWindow::~AppWindow()
{
    delete ui;
}

