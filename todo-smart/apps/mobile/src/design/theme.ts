import { colors } from "./tokens/colors";
import { spacing } from "./tokens/spacing";
import { typography } from "./tokens/typography";
import { radius } from "./tokens/radius";
import { shadows } from "./tokens/shadows";

export const theme = { colors, spacing, typography, radius, shadows };
export type Theme = typeof theme;
