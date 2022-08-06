import faker from "./faker";
import helper from "./helper";
import lodash from "./lodash";
import colors from "./colors";
// import axios from "./axios"
// import process_axios_error from './axios_error'

export default (app) => {
  app.use(faker);
  app.use(helper);
  app.use(lodash);
  app.use(colors);
  // app.use(axios);
  // app.use(process_axios_error)
};
