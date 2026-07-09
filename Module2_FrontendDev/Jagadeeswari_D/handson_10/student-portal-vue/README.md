# student-portal-vue

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```



# Hands-On 10 – API Integration & Advanced State Management

## Framework Comparison

### React + Redux Toolkit
- Uses a centralized Redux store.
- Supports async API calls using createAsyncThunk.
- Selectors help components access state.
- More boilerplate than Vue.

### Angular + NgRx
- Uses Actions, Reducers, Effects, and Selectors.
- Effects handle API calls.
- Best suited for large enterprise applications.

Data Flow:
Component → Action → Effect → API → Reducer → Store → Selector → Component

### Vue + Pinia
- Official state management library for Vue.
- Minimal boilerplate.
- Reactive by default.
- Easy integration with Composition API.

### Features Implemented
- Centralized API Layer
- Axios Request & Response Interceptors
- Authorization Header
- fetchAndEnroll() action
- resetEnrollment() action
- storeToRefs()
- Global Error Handler