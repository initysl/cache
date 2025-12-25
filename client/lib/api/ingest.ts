import { apiClient } from './api';
import { IngestRequest, IngestResponse } from '@/types';

export const ingestApi = {
  ingest: async (payload: IngestRequest): Promise<IngestResponse> => {
    try {
      const response = await apiClient.post<IngestResponse>('/ingest', payload);
      return response.data;
    } catch (error) {
      console.error('Error ingesting document:', error);
      throw error;
    }
  },
};
