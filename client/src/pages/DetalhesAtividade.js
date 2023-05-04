import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './DetalhesAtividade.css';
import Nav from '../components/Nav'; 

function AtividadeDetalhes(props) {
  const [atividade, setAtividade] = useState(null);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/atividades/${props.match.params.id}`).then(response => {
        setAtividade(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [props.match.params.id]);

  if (!atividade) {
    return <div>Carregando...</div>;
  }

  return (
    <div className="atividade-detalhes">
      <header>
        <Nav /> 
      </header>
      <div className="imagem">
        <img src={atividade.imagem_url} alt={atividade.nome} />
      </div>
      <div className="info">
        <h1>{atividade.nome}</h1>
        <p>{atividade.descricao}</p>
        <p>{atividade.localizacao}</p>
        <p>{atividade.horario_funcionamento}</p>
      </div>
    </div>
  );
}

export default AtividadeDetalhes;

