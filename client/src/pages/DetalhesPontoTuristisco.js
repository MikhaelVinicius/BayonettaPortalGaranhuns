import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../CSS/DetalhesPontoTuristico.css';
import Nav from '../components/Nav'; 

function PontoTuristicoDetalhes(props) {
  const [pontosTuristicos, setPontosTuristicos] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/pontos_turisticos/${props.match.params.id}`).then(response => {
      setPontosTuristicos(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [props.match.params.id]);

  if (!pontosTuristicos) {
    return <div>Carregando...</div>;
  }

  return (
    <div className="atividade-detalhes">
      <header>
        <Nav /> 
      </header>
      <h1>OLá</h1>
      <div className="imagem">
        <img src={pontosTuristicos.imagem_url} alt={pontosTuristicos.nome} />
      </div>
      <div className="info">
        <h1>{pontosTuristicos.nome}</h1>
        <p>{pontosTuristicos.descricao}</p>
        <p>{pontosTuristicos.localizacao}</p>
     
      </div>
    </div>
  );
}

export default PontoTuristicoDetalhes;

