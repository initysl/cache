import { apiClient } from './api';
import { SearchRequest, SearchResponse } from '@/types';

export const searchApi = {
  search: async (payload: SearchRequest): Promise<SearchResponse> => {
    const response = await apiClient.post<SearchResponse>(
      '/search',
      payload
    );
    return response.data;
  },
};
