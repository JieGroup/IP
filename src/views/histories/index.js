const linkTo = (name, router, params) => {
  router.push({
    name: name,
    params: params
  });
};

export { linkTo };