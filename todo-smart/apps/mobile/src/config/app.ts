import { env } from "./env";

export const appConfig = {
  name: env.APP_NAME,
  locale: "fa-IR",
  direction: "rtl",
} as const;
