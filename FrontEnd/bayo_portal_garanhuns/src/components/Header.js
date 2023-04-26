import { Navbar, Nav, Container } from 'react-bootstrap';
import './Header.css';
import brasao from '../assents/brasao.png';

function Header() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg" className="navbar">
      <Container>
        <Navbar.Brand href="#" className="navbar-brand">
          <img src={brasao} alt="Brasão de Garanhuns" className="brand-logo" />
          Portal de Turismo de Garanhuns
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbar-nav" />
        <Navbar.Collapse id="navbar-nav">
          <Nav className="ml-auto">
            <Nav.Link href="#" className="nav-link">
              Pontos Turísticos
            </Nav.Link>
            <Nav.Link href="#" className="nav-link">
              Restaurantes
            </Nav.Link>
            <Nav.Link href="#" className="nav-link">
              Hotéis/Pousadas
            </Nav.Link>
            <Nav.Link href="#" className="nav-link">
              Eventos
            </Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
