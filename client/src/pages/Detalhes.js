import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Detalhes.css';

function Detalhes(props) {
  const [local, setLocal] = useState(null);
  const [comentarios, setComentarios] = useState([]);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/${props.tipo}/${props.id}`).then(response => {
        setLocal(response.data);
      })
      .catch(error => {
        console.log(error);
      });

    axios.get(`http://127.0.0.1:5000/api/${props.tipo}/${props.id}/comentarios`).then(response => {
        setComentarios(response.data);
      })
      .catch(error => {
        console.log(error);
      });
  }, [props.id, props.tipo]);

  if (!local) {
    return <div>Carregando...</div>;
  }

  return (
    <div className="detalhes">
      <h1>{local.nome}</h1>
      <div className="imagens">
        <img src={local.imagem_url} alt={local.nome} />
        {local.outras_imagens.map(imagem => (
          <img src={imagem} alt={local.nome} key={imagem} />
        ))}
      </div>
      <div className="informacoes">
        <h2>Informações</h2>
        {local.descricao && (
          <div>
            <h3>Descrição</h3>
            <p>{local.descricao}</p>
          </div>
        )}
        {local.endereco && (
          <div>
            <h3>Endereço</h3>
            <p>{local.endereco}</p>
          </div>
        )}
        {local.telefone && (
          <div>
            <h3>Telefone</h3>
            <p>{local.telefone}</p>
          </div>
        )}
        {local.website && (
          <div>
            <h3>Website</h3>
            <p>{local.website}</p>
          </div>
        )}
        {local.horario_funcionamento && (
          <div>
            <h3>Horário de funcionamento</h3>
            <p>{local.horario_funcionamento}</p>
          </div>
        )}
      </div>
      <div className="comentarios">
        <h2>Comentários</h2>
        <ul>
          {comentarios.map(comentario => (
            <li key={comentario.id}>
              <p>{comentario.texto}</p>
              <p>Por {comentario.usuario} em {new Date(comentario.data).toLocaleString()}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Detalhes;
