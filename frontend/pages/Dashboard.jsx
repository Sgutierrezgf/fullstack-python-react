import { Outlet, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

function DashboardLayout() {
    const { user } = useAuth();

    return (
        <div>
            <nav style={{ background: "#333", padding: "10px" }}>
                <ul style={{ display: "flex", justifyContent: "space-around", listStyle: "none", margin: 0, padding: 0 }}>
                    <li>
                        <Link to="/products" style={{ color: "white", textDecoration: "none", fontSize: "16px" }}>
                            Productos
                        </Link>
                    </li>
                    {user?.role === "admin" && (
                        <li>
                            <Link to="/users" style={{ color: "white", textDecoration: "none", fontSize: "16px" }}>
                                Usuarios
                            </Link>
                        </li>
                    )}
                </ul>
            </nav>
            <div style={{ padding: "20px" }}>
                <Outlet />
            </div>
        </div>
    );
}

export default DashboardLayout;
