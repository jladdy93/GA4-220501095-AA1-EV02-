from views.crud_view import CrudView
import services.usuario_service as usuario_service


if __name__ == "__main__":
    app = CrudView()
    app.mainloop()