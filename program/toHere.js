export const updateMySpace = (title, description, backgroundColor, color) => {
  return async (dispatch, getState) => {
    try {
      const user = getState().user;
      let token, space;

      if (user && user.profile && user.profile.space) {
        token = user.token;
        space = user.profile.space;
      }

      dispatch(appLoading());

      const response = await axios.patch(
        `${apiUrl}/auth/${space.id}`,
        {
          title,
          description,
          backgroundColor,
          color,
        },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      dispatch(
        showMessageWithTimeout("success", false, "update successfull", 3000)
      );
      dispatch(spaceUpdated(response.data.space));
      dispatch(appDoneLoading());
    } catch (error) {
      if (error.response) {
        console.log(error.response.data.message);
        dispatch(
          setMessage({
            variant: "danger",
            dismissable: true,
            text: error.response.data.message,
          })
        );
      } else {
        console.log(error.message);
        dispatch(
          setMessage({
            variant: "danger",
            dismissable: true,
            text: error.response.data.message,
          })
        );
      }
      dispatch(appDoneLoading());
    }
  };
};
