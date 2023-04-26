// Header.js

import React from 'react';
import { Navbar, Nav, Container } from 'react-bootstrap';
import './Header.css'; // Importar o arquivo CSS

function Header() {
  return (
    <Navbar bg="light" expand="lg" className="navbar">
      <Container>
        <Navbar.Brand href="#" className="navbar-brand">
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
              Hoteis/Pousadas
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
