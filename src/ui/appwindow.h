#pragma once

#include <QMainWindow>

QT_BEGIN_NAMESPACE
namespace Ui {
class AppWindow;
}
QT_END_NAMESPACE

class AppWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit AppWindow(QWidget *parent = nullptr);
    ~AppWindow() override;

private slots:

private:
    Ui::AppWindow *ui;
};

