import { apiUrl } from "../../config/constants";
import axios from "axios";
import { selectToken } from "./selectors";
import { appLoading, appDoneLoading, setMessage } from "../appState/slice";
import { showMessageWithTimeout } from "../appState/thunks";

import {
  loginSuccess,
  logOut,
  tokenStillValid,
  deleteStoreStory,
  saveStoreStory,
  spaceUpdated,
} from "./slice";

export const signUp = (name, email, password) => {
  return async (dispatch, getState) => {
    // Loading icon
    dispatch(appLoading());
    try {
      const response = await axios.post(`${apiUrl}/auth/signup`, {
        name,
        email,
        password,
      });

      // Store data in redux and JWT to local storage.
      dispatch(
        loginSuccess({ token: response.data.token, user: response.data.user })
      );

      // Show the message (located in appState).
      dispatch(showMessageWithTimeout("success", true, "account created"));
      dispatch(appDoneLoading());
    } catch (error) {
      // Handle the error correctly with the same kind of message as above.
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
            text: error.message,
          })
        );
      }
      dispatch(appDoneLoading());
    }
  };
};

export const login = (email, password) => {
  return async (dispatch, getState) => {
    dispatch(appLoading());
    try {
      const response = await axios.post(`${apiUrl}/auth/login`, {
        email,
        password,
      });

      // If okay, store data and JWT
      dispatch(
        loginSuccess({ token: response.data.token, user: response.data.user })
      );

      dispatch(showMessageWithTimeout("success", false, "welcome back!", 1500));
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

export const getUserWithStoredToken = () => {
  return async (dispatch, getState) => {
    // get token from the state
    const token = selectToken(getState());

    // if we have no token, stop
    if (token === null) return;

    dispatch(appLoading());
    try {
      // if we do have a token,
      // check wether it is still valid or if it is expired
      const response = await axios.get(`${apiUrl}/auth/me`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      // token is still valid
      dispatch(tokenStillValid({ user: response.data }));
      dispatch(appDoneLoading());
    } catch (error) {
      if (error.response) {
        console.log(error.response.message);
      } else {
        console.log(error);
      }
      // if we get a 4xx or 5xx response,
      // get rid of the token by logging out
      dispatch(logOut());
      dispatch(appDoneLoading());
    }
  };
};

export const deleteStory = (id) => {
  return async (dispatch, getState) => {
    // Always check if logged in, since this should be a protected endpoint.
    const token = selectToken(getState());

    if (!token) return;

    dispatch(appLoading());
    try {
      await axios.delete(`${apiUrl}/spaces/mySpace/stories/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });

      // Delete the story from redux state, component will rerender (redux manages that).
      dispatch(deleteStoreStory(id));
      dispatch(appDoneLoading());
    } catch (error) {
      console.log(error.message);
      // if (error.response) {
      //   console.log(error.response.data.message);
      //   dispatch(
      //     setMessage({
      //       variant: "danger",
      //       dismissable: true,
      //       text: error.response.data.message,
      //     })
      //   );
      // } else {
      //   console.log(error.message);
      //   dispatch(
      //     setMessage({
      //       variant: "danger",
      //       dismissable: true,
      //       text: error.response.data.message,
      //     })
      //   );
      // }
      dispatch(appDoneLoading());
    }
  };
};

export const saveStory = (name, content, spaceId) => {
  return async (dispatch, getState) => {
    const token = selectToken(getState());

    if (!token) return;

    dispatch(appLoading());
    try {
      const response = await axios.post(
        `${apiUrl}/spaces/mySpace/stories/new`,
        {
          name,
          content,
          spaceId,
          headers: { Authorization: `Bearer ${token}` },
        }
      );
      dispatch(saveStoreStory(response.data.newStory));
      dispatch(
        showMessageWithTimeout("success", false, "Story is created!", 1500)
      );
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
