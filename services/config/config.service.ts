export interface ConfigService {
  getConfig<T>(configKey: string, env: string): Promise<T>;
}

export function createConfigService(db: any): ConfigService {
  return {
    async getConfig(configKey, env) {
      const result = await db.query(
        `
        SELECT config_value
        FROM system_config
        WHERE config_key = $1
          AND environment = $2
          AND is_active = true
        ORDER BY version DESC
        LIMIT 1
        `,
        [configKey, env]
      );

      if (!result.rows.length) {
        throw new Error("CONFIG_NOT_FOUND");
      }

      return result.rows[0].config_value;
    },
  };
}
