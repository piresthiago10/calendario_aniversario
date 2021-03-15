<template>
  <div class="content">
    <h2>{{ titulo }}</h2>
    <p v-show="mensagem" class="centralizado">{{ mensagem }}</p>
    <input
      type="search"
      class="field"
      @:input="filtro = $event.target.value"
      placeholder="Filtre pela data de aniversário"
    />
    {{ filtro }}

    <tabela-aniversario :titulo="aniversarios.nome">
      <tr v-for="aniversario of aniversariosComFiltro">
        <td>01</td>
        <td>teste</td>
        <td>21/07/1997</td>
        <td>
          <router-link :to="{ name: 'cadastro', params: { id : aniversario.id }} ">
            <meu-botao rotulo="Alterar" tipo="button" />
          </router-link>
          <meu-botao
            rotulo="remover"
            tipo="button"
            :confirmacao="true"
            @botaoAtivado="remove(aniversario)"
            estilo="perigo"
          />
        </td>
      </tr>
    </tabela-aniversario>
  </div>
</template>

<script>
import Aniversarios from "../shared/aniversario/Aniversario.vue";
import Botao from "../shared/botao/Botao.vue";

import AniversarioService from "../../domain/aniversario/AniversarioService.js";

export default {
  components: {
    "tabela-aniversario": Aniversarios,
    "meu-botao": Botao,
  },

  data() {
    return {
      titulo: "Lista de Aniversários",
      aniversarios: [],
      filtro: "",
      mensagem: "",
    };
  },

  computed: {
    aniversariosComFiltro() {
      if (this.filtro) {
        let exp = new RegExp(this.filtro.trim(), "i");
        return this.aniversarios.filter((aniversario) =>
          exp.test(aniversario.data_aniversario)
        );
      } else {
        return this.aniversarios;
      }
    },
  },

  methods: {
    remove(aniversario) {
      this.service.apaga(aniversario.id).then(
        () => {
          let indice = this.aniversarios.ondexOf(aniversario);
          this.aniversarios.splice(indice, 1);
          this.mensagem = "Aniversário removido com sucesso";
        },
        err => this.mensagem = err.message
      );
    },
  },

  created() {
    this.service = new AniversarioService(this.$resource);

    this.service
      .lista()
      .then(
        (aniversarios) =>
          (this.aniversarios = (aniversarios) => console.log(err)),
          err => this.mensagem = err.message

      );
  },
};
</script>

<style>
body {
  background-color: #f2f2f2;
}

.field {
  display: block;
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  box-sizing: border-box;
  font-size: 1.2em;
}
</style>
