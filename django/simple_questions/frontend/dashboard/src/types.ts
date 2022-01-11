export interface AccountResponse {
    user: {
      id: string;
      email: string;
      display_name: string;
      username: string;
      created_at: Date;
      updated_at: Date;
    };
    access: string;
    refresh: string;
  }