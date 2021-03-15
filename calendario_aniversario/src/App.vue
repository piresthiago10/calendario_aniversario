<template>
  <div class="content">

    <topo-menu :rotas="routes">

    </topo-menu>
  
    <transition name="pagina">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
import { routes } from "./routes";
import Menu from './components/shared/menu/Menu.vue';

export default {

  components: {
    'topo-menu': Menu
  },

  data() {
    return {
      routes: routes.filter(route => route.menu)
    };
  },
};
</script>

<style>
.content {
  font-family: "Courier New", Courier, monospace;
  width: 90%;
  margin: 0 auto;
}

.pagina-enter-active,
.pagina-leave-active {
  transition: opacity 0.3s;
}
.pagina-enter,
.pagina-leave-active {
  opacity: 0;
}
</style>
