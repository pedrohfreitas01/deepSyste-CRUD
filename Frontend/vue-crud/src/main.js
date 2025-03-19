import { createApp } from "vue";
import App from "./App.vue";
import PrimeVue from "primevue/config";
import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import router from "./router";

// Importe os componentes do PrimeVue
import Button from "primevue/button";
import DataTable from "primevue/datatable";
import Column from "primevue/column";
import InputText from "primevue/inputtext";
import Dropdown from "primevue/dropdown";
import Checkbox from "primevue/checkbox";
import Dialog from "primevue/dialog";

const app = createApp(App);

//  componentes globalmente
app.component("Button", Button);
app.component("DataTable", DataTable);
app.component("Column", Column);
app.component("InputText", InputText);
app.component("Dropdown", Dropdown);
app.component("Checkbox", Checkbox);
app.component("Dialog", Dialog);

app.use(PrimeVue);
app.use(router);
app.mount("#app");
