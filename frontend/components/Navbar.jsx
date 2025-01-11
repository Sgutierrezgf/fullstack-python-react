import { Link } from "react-router-dom";

function Navbar() {
    return (
        <nav style={{ background: '#333', padding: '10px' }}>
            <ul style={{ display: 'flex', justifyContent: 'space-around', listStyleType: 'none', margin: 0, padding: 0 }}>
                <li>
                    <Link to="/users" style={{ color: 'white', textDecoration: 'none', fontSize: '16px' }}>
                        Usuarios
                    </Link>
                </li>
                <li>
                    <Link to="/products" style={{ color: 'white', textDecoration: 'none', fontSize: '16px' }}>
                        Productos
                    </Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
