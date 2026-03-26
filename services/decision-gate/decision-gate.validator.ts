import {
  DecisionGateInput,
  DecisionGateOutput,
  PerformanceStatus,
} from "./decision-gate.types";

const VALID_STATUSES: PerformanceStatus[] = [
  "scale",
  "observe",
  "iterate",
  "cooldown",
  "terminate",
];

export function validateDecisionGateInput(input: unknown): boolean {
  if (!input || typeof input !== "object") return false;

  const i = input as any;

  if (typeof i.vertical_id !== "string") return false;
  if (typeof i.environment !== "string") return false;

  if (!i.payload || typeof i.payload !== "object") return false;

  if (!
